from alpaca.device import Device
from alpaca.telescope import GuideDirections
from enum import Enum
from typing import List, Any

class CameraStates(Enum):
    cameraIdle      = 0
    cameraWaiting   = 1
    cameraExposing  = 2
    cameraReading   = 3
    cameraDownload  = 4
    cameraError     = 5

class SensorTypes(Enum):    # **TODO** This is singular in the spec
    Monochrome      = 0
    Color           = 1
    RGGB            = 2
    CMYG            = 3
    CMYG2           = 4
    LRGB            = 5



class Camera(Device):
    """ASCOM Standard iCamera V3 Interface."""

    def __init__(
        self,
        address: str,
        device_number: int,
        protocol: str = "http"
    ):
        """Initialize Camera object."""
        super().__init__(address, "camera", device_number, protocol)

    @property
    def BayerOffsetX(self) -> int:
        """Return the X offset of the Bayer matrix, as defined in SensorType."""
        return self._get("bayeroffsetx")

    @property
    def BayerOffsetY(self) -> int:
        """Return the Y offset of the Bayer matrix, as defined in SensorType."""
        return self._get("bayeroffsety")

    @property
    def BinX(self) -> int:
        """Set or return the binning factor for the X axis.

        Args:
            BinX (int): The X binning value.
        
        Returns:
            Binning factor for the X axis.
        
        """
        return self._get("binx")
    @BinX.setter
    def BinX(self, BinVal: int):
        self._put("binx", BinX=BinVal)

    @property
    def BinY(self) -> int:
        """Set or return the binning factor for the Y axis.

        Args:
            BinY (int): The Y binning value.
        
        Returns:
            Binning factor for the Y axis.
        
        """
        return self._get("biny")
    @BinY.setter
    def BinY(self, BinVal: int):
        self._put("biny", BinY=BinVal)

    @property
    def CameraState(self) -> CameraStates:
        """Return the camera operational state (enum CameraStates).

        CameraStates values:
            0 = CameraIdle, 1 = CameraWaiting, 2 = CameraExposing,
            3 = CameraReading, 4 = CameraDownload, 5 = CameraError.
        
        Returns:
            Current camera operational state (enum CameraStates).
        
        """
        return self._get("camerastate")

    @property
    def CameraXSize(self) -> int:
        """Return the width (int) of the CCD camera chip."""
        return self._get("cameraxsize")

    @property
    def CameraYSize(self) -> int:
        """Return the height (int) of the CCD camera chip."""
        return self._get("cameraysize")

    @property
    def CanAbortExposure(self) -> bool:
        """Indicate whether the camera can abort exposures."""
        return self._get("canabortexposure")

    @property
    def CanAsymmetricBin(self) -> bool:
        """Indicate whether the camera supports asymmetric binning."""
        return self._get("canasymmetricbin")

    @property
    def CanFastReadout(self) -> bool:
        """Indicate whether the camera has a fast readout mode."""
        return self._get("canfastreadout")

    @property
    def CanGetCoolerPower(self) -> bool:
        """Indicate whether the camera's cooler power setting can be read."""
        return self._get("cangetcoolerpower")

    @property
    def CanPulseGuide(self) -> bool:
        """Indicate whether this camera supports pulse guiding."""
        return self._get("canpulseguide")

    @property
    def CanSetCCDTemperature(self) -> bool:
        """Indicate whether this camera supports setting the CCD temperature."""
        return self._get("cansetccdtemperature")

    @property
    def CanStopExposure(self) -> bool:
        """Indicate whether this camera can stop an exposure that is in progress."""
        return self._get("canstopexposure")

    @property
    def CCDTemperature(self) -> float:
        """Return the current CCD temperature in degrees Celsius."""
        return self._get("ccdtemperature")

    @property
    def CoolerOn(self) -> bool:
        """Turn the camera cooler on and off or return the current cooler on/off state.

        Notes:
            True = cooler on, False = cooler off.

        Args:
            CoolerOn (bool): Cooler state.
        
        Returns:
            Current cooler on/off state.
        
        """
        return self._get("cooleron")
    @CoolerOn.setter
    def CoolerOn(self, CoolerState: bool):
        self._put("cooleron", CoolerOn=CoolerState)

    @property
    def CoolerPower(self) -> float:
        """Return the present cooler power level, in percent."""
        return self._get("coolerpower")

    @property
    def ElectronsPerADU(self) -> float:
        """Return the gain of the camera (float) in photoelectrons per A/D unit."""
        return self._get("electronsperadu")

    @property
    def ExposureMax(self) -> float:
        """Return the maximum exposure time (float) supported by StartExposure."""
        return self._get("exposuremax")

    @property
    def ExposureMin(self) -> float:
        """Return the minimum exposure time (float) supported by StartExposure."""
        return self._get("exposuremin")

    @property
    def ExposureResolution(self) -> float:
        """Return the smallest increment in exposure time (float) supported by StartExposure."""
        return self._get("exposureresolution")

    @property
    def FastReadout(self) -> bool:
        """Set or return whether Fast Readout Mode is enabled.

        Args:
            FastReadout (bool): True to enable fast readout mode.
        
        Returns:
            Whether Fast Readout Mode is enabled.

        """
        return self._get("fastreadout")
    @FastReadout.setter
    def FastReadout(self, FastReadout: bool):
        self._put("fastreadout", FastReadout=FastReadout)

    @property
    def FullWellCapacity(self) -> float:
        """Report the full well capacity of the camera.

        Report the full well capacity of the camera in electrons, at the current
        camera settings (binning, SetupDialog settings, etc.).

        Returns:
            Full well capacity of the camera.

        """
        return self._get("fullwellcapacity")

    @property
    def Gain(self) -> int:
        """Set or return an index into the Gains array.

        Args:
            Gain (int): Index of the current camera gain in the Gains array.
        
        Returns:
            Index into the Gains array for the selected camera gain.
        
        """
        return self._get("gain")
    @Gain.setter
    def Gain(self, Gain: int):
        self._put("gain", Gain=Gain)

    @property
    def GainMax(self) -> int:
        """Maximum value of Gain."""
        return self._get("gainmax")

    @property
    def GainMin(self) -> int:
        """Minimum value of Gain."""
        return self._get("gainmin")

    @property
    def Gains(self) -> List[int]:
        """Gains supported by the camera."""
        return self._get("gains")

    @property
    def HasShutter(self) -> bool:
        """Indicate whether the camera has a mechanical shutter."""
        return self._get("hasshutter")

    @property
    def HeatSinkTemperature(self) -> float:
        """Return the current heat sink temperature.

        Returns:
            Current heat sink temperature (called "ambient temperature" by some
            manufacturers) in degrees Celsius.

        """
        return self._get("heatsinktemperature")

    @property
    def ImageArray(self) -> List[int]:
        """Return an array of integers containing the exposure pixel values.

        Return an array of 32bit integers containing the pixel values from the last
        exposure. This call can return either a 2 dimension (monochrome images) or 3
        dimension (colour or multi-plane images) array of size NumX * NumY or NumX *
        NumY * NumPlanes. Where applicable, the size of NumPlanes has to be determined
        by inspection of the returned Array. Since 32bit integers are always returned
        by this call, the returned JSON Type value (0 = Unknown, 1 = short(16bit),
        2 = int(32bit), 3 = Double) is always 2. The number of planes is given in the
        returned Rank value. When de-serialising to an object it helps enormously to
        know the array Rank beforehand so that the correct data class can be used. This
        can be achieved through a regular expression or by direct parsing of the
        returned JSON string to extract the Type and Rank values before de-serialising.
        This regular expression accomplishes the extraction into two named groups Type
        and Rank ^*"Type":(?<Type>\d*),"Rank":(?<Rank>\d*) which can then be used to
        select the correct de-serialisation data class.

        Returns:
            Array of integers containing the exposure pixel values.

        **TODO** Form the array in Python

        """
        return self._get("imagearray")

    @property
    def ImageArrayVariant(self) -> List[int]:
        """Return an array of integers containing the exposure pixel values.

        Return an array of 32bit integers containing the pixel values from the last
        exposure. This call can return either a 2 dimension (monochrome images) or 3
        dimension (colour or multi-plane images) array of size NumX * NumY or NumX *
        NumY * NumPlanes. Where applicable, the size of NumPlanes has to be determined
        by inspection of the returned Array. This call can return values as 
        short(16bit) integers, int(32bit) integers or double floating point values. 
        The nature of the returned values is given in the Type parameter: 0 = Unknown, 
        1 = short(16bit), 2 = int(32bit), 3 = Double. The number of planes is given in
        the returned Rank value. PLEASE REFER TO ALPACA DOCUMENTATION FOR MORE DETAILS
        INCLUDING COLOR/BAYER FORMATTING AND HIGH-SPEED IMAGEBYTES IMAGE DATA.

        Returns:
            Array of integers containing the pixel values from the last exposure.

        **TODO** Form the array in Python
        
        """
        return self._get("imagearrayvariant")

    @property
    def ImageReady(self) -> bool:
        """Indicates that an image is ready to be downloaded."""
        return self._get("imageready")

    @property
    def IsPulseGuiding(self) -> bool:
        """Indicatee that the camera is pulse guideing."""
        return self._get("ispulseguiding")

    @property
    def LastExposureDuration(self) -> float:
        """Report the actual exposure duration in seconds (i.e. shutter open time)."""
        return self._get("lastexposureduration")

    @property
    def LastExposureStartTime(self) -> str:
        """Start time of the last exposure in FITS standard format.
        
        Reports the actual exposure start in the FITS-standard / ISO-8601
        CCYY-MM-DDThh:mm:ss[.sss...] format.

        Returns:
            Start time of the last exposure in FITS / ISO-8601 standard format.

        """
        return self._get("lastexposurestarttime")

    @property
    def MaxAdu(self) -> int:
        """Camera's maximum ADU value."""
        return self._get("maxadu")

    @property
    def MaxBinX(self) -> int:
        """Maximum binning for the camera X axis."""
        return self._get("maxbinx")

    @property
    def MaxBinY(self) -> int:
        """Maximum binning for the camera Y axis."""
        return self._get("maxbiny")

    @property
    def NumX(self) -> int:
        """Set or return the current subframe width.
        
        Args:
            NumX (int): Subframe width, if binning is active, value is in binned
                pixels.
        
        Returns:
            Current subframe width.
        
        """
        return self._get("numx")
    @NumX.setter
    def NumX(self, NumX: int):
        self._put("numx", NumX=NumX)

    @property
    def NumY(self) -> int:
        """Set or return the current subframe height.
        
        Args:
            NumX (int): Subframe height, if binning is active, value is in binned
                pixels.
        
        Returns:
            Current subframe height.
        
        """
        return self._get("numy")
    @NumY.setter
    def NumY(self, NumY: int):
        self._put("numy", NumY=NumY)

    @property
    def Offset(self) -> int:
        """Set or return an index into the Offsets array.

        Args:
            Offset (int): Index of the current camera offset in the Offsets array.
        
        Returns:
            Index into the Offsets array for the selected camera offset.
        
        """
        return self._get("offset")
    @Offset.setter
    def Offset(self, Offset: int):
        self._put("offset", Offset=Offset)

    @property
    def OffsetMax(self) -> int:
        """Maximum value of Offset."""
        return self._get("offsetmax")

    @property
    def OffsetMin(self) -> int:
        """Minimum value of Offset."""
        return self._get("offsetmin")

    @property
    def Offsets(self) -> List[int]:
        """Offsets supported by the camera."""
        return self._get("offsets")

    @property
    def PercentCompleted(self) -> int:
        """Indicate percentage completeness of the current operation.

        Returns:
            An integer between 0 and 100% indicating the completeness of 
            this operation.

        """
        return self._get("percentcompleted")

    @property
    def PixelSizeX(self):
        """Width of CCD chip pixels (microns)."""
        return self._get("pixelsizex")

    @property
    def PixelSizeY(self):
        """Height of CCD chip pixels (microns)."""
        return self._get("pixelsizey")

    @property
    def ReadoutMode(self) -> int:
        """Set or get the canera's readout mode as an index into the array ReadoutModes."""
        return self._get("readoutmode")
    @ReadoutMode.setter
    def ReadoutMode(self, ReadoutMode: int):
        self._put("readoutmode", ReadoutMode=ReadoutMode)

    @property
    def ReadoutModes(self) -> List[str]:
        """List of available readout mode names.
        
        Notes:
            The names are indexed, and the index of the name is used to
            set and get the current readout mode.

        """
        return self._get("readoutmodes")

    @property
    def SensorName(self) -> str:
        """Name of the sensor used within the camera."""
        return self._get("sensorname")

    @property
    def SensorType(self) -> SensorTypes:
        """Type of information returned by the the camera sensor (monochrome or colour).
        
        Returns: Enum SensorTypes: 
            0 = Monochrome, 
            1 = Colour (not requiring Bayer decoding)
            2 = RGGB   (Bayer encoding)
            3 = CMYG   (Bayer encoding)
            4 = CMYG2  (Bayer encoding)
            5 = LRGB   TRUESENSE Bayer encoding
       
        """
        return self._get("sensortype")
    
    @property
    def SetCCDTemperature(self) -> float:
        """Set or return the camera's cooler setpoint (degrees Celsius).

        Args:
            SetCCDTemperature (float): 	Temperature set point (degrees Celsius).
        
        Returns:
            Camera's cooler setpoint (degrees Celsius).
        
        """
        return self._get("setccdtemperature")
    @SetCCDTemperature.setter
    def SetCCDTemperature(self, SetCCDTemperature: float):
        self._put("setccdtemperature", SetCCDTemperature=SetCCDTemperature)

    @property
    def StartX(self) -> int:
        """Set or return the current subframe X axis start position.

        Args:
            StartX (int): The subframe X axis start position in binned pixels.
        
        Returns:
            Sets the subframe start position for the X axis (0 based) and returns the
            current value. If binning is active, value is in binned pixels.
        
        """
        return self._get("startx")
    @StartX.setter
    def StartX(self, StartX: int):
        self._put("startx", StartX=StartX)

    @property
    def StartY(self) -> int:
        """Set or return the current subframe Y axis start position.

        Args:
            StartY (int): The subframe Y axis start position in binned pixels.
        
        Returns:
            Sets the subframe start position for the Y axis (0 based) and returns the
            current value. If binning is active, value is in binned pixels.
        
        """
        return self._get("starty")
    @StartY.setter
    def StartY(self, StartY):
        self._put("starty", StartY=StartY)

    @property
    def SubExposureDuration(self) -> float:
        """Camera's sub-exposure interval (float)

        The Camera's sub exposure duration (float) in seconds. Only available in Camera 
        Interface Version 3 and later.

        """
        return self._get("subexposureduration")
    @SubExposureDuration.setter
    def SubExposureDuration(self, SubexposureDuration: float):
        self._put("subexposureduration", SubexposureDuration=SubexposureDuration)

    def AbortExposure(self) -> None:
        """Abort the current exposure, if any, and returns the camera to Idle state."""
        self._put("abortexposure")

    def PulseGuide(self, Direction: GuideDirections, Duration: int) -> None:
        """Pulse guide in the specified direction for the specified time (ms).
        
        Args:
            Direction (enum GuideDirections): Direction of movement 
                (0 = North, 1 = South, 2 = East, 3 = West).
            Duration (int): Duration of movement in milli-seconds.
        **TODO** Check this once the Telescope PulseGuide is working
        """
        self._put("pulseguide", Direction=Direction, Duration=Duration)

    def StartExposure(self, Duration: float, Light: bool) -> None:
        """Start an exposure. Returns if exposure has successfully been started.
        
        Notes:
            Asynchronous Use ImageReady to check when the exposure has been
            successfully completed.
        
        Args:
            Duration (float): Duration of exposure in seconds.
            Light (bool): True if light frame, false if dark frame.

        """
        self._put("startexposure", Duration=Duration, Light=Light)

    def StopExposure(self) -> None:
        """Stop the current exposure, if any.
        
        Notes:
            If an exposure is in progress, the readout process is initiated. Ignored if
            readout is already in process.
        
        """
        self._put("stopexposure")
